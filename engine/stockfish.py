import os
import queue
import subprocess
import threading

_LEVELDATA = (
    (0, 10, 1),
    (6, 160, 4),
    (12, 500, 10),
)


def get_fish_path():
    conf = os.path.join("src", "stockfish", "path.txt")
    if os.path.exists(conf):
        with open(conf, "r") as f:
            return f.read().strip()


def rm_fish_path():
    os.remove(os.path.join("src", "stockfish", "path.txt"))


class StockFish:
    def __init__(self, path="stockfish", level=1):
        self.moves = []
        self.skill, self.movetime, self.depth = _LEVELDATA[level - 1]

        self.thread = threading.Thread()
        self.q = queue.Queue(1)

        try:
            self.stockfish = subprocess.Popen(
                path,
                universal_newlines=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
            )

            if self.stockfish.stdout.readline().split()[0].lower() == "stockfish":
                self.active = True
                self._put("uci")
                self.set_option("Skill Level", self.skill)
            else:
                self.active = False
                self.stockfish.terminate()

        except:
            self.active = False

    def _raise_error_if_inactive(self):
        if not self.active:
            raise RuntimeError("Intergration with stockfish engine has failed")

    def _put(self, command):
        self._raise_error_if_inactive()
        self.stockfish.stdin.write(str(command) + "\n")
        self.stockfish.stdin.flush()

    def _is_ready(self):
        self._raise_error_if_inactive()
        self._put("isready")
        while True:
            if self.stockfish.stdout.readline().strip() == "readyok":
                return

    def _engine(self):
        self._is_ready()
        self._put("position startpos moves " + " ".join(self.moves))
        self._put("go depth {} movetime {}".format(self.depth, self.movetime))
        while True:
            msg = self.stockfish.stdout.readline().strip().split(" ")
            if msg[0] == "bestmove":
                if msg[1] == "(none)":
                    self.q.put(None)
                else:
                    self.q.put(msg[1])
                break

    def is_active(self):
        return self.active

    def start_game(self, moves=""):
        self._is_ready()
        self._put("ucinewgame")
        self.moves = moves.split()

    def set_option(self, name, value):
        self._is_ready()
        self._put("setoption name {} value {}".format(name, value))

    def start_engine(self):
        self._raise_error_if_inactive()
        if not self.thread.is_alive() and self.q.empty():
            self.thread = threading.Thread(target=self._engine)
            self.thread.start()
        else:
            raise RuntimeError("Could not start engine")

    def make_move(self, move):
        self.moves.append(move)
        self.start_engine()

    def get_move(self, block=True):
        self._raise_error_if_inactive()
        if not self.has_moved() and not block:
            self._put("stop")
        print(list(self.q.queue))
        enginemove = self.q.get()
        self.moves.append(enginemove)
        return enginemove

    def has_moved(self):
        self._raise_error_if_inactive()
        return not self.q.empty() and not self.thread.is_alive()

    def undo(self, num=1):
        self._raise_error_if_inactive()
        if not self.thread.is_alive():
            if len(self.moves) not in range(num):
                self.moves = self.moves[:-num]

    def close(self):
        self._is_ready()
        self._put("quit")
        self.stockfish.terminate()
        self.active = False
