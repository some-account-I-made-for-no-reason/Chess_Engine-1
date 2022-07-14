import Fen_reader
import Engine

def getCoords():
    Coords = [['a8','b8','c8','b8','e8','f8','g8','h8'],
                         ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
                         ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
                         ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
                         ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
                         ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
                         ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
                         ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']]
    return Coords

def placePieces(fen_):
    default_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    if fen_ != 'd' :
        return Fen_reader.fen_to_board(fen_)
    else :
        return Fen_reader.fen_to_board(default_fen)

gs = Engine.GameState()
m1 = Engine.Move('e2','e4',gs)
print(gs.push(m1))
