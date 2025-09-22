def evaluate(self):
        if self.board.is_checkmate():
            if self.board.turn == chess.WHITE:
                return -1000
            else:
                return 1000
        if self.board.is_stalemate() or self.board.is_insufficient_material() or self.board.can_claim_draw():
            return 0

        score = 0
        values = {chess.PAWN:1, chess.KNIGHT:3, chess.BISHOP:3, chess.ROOK:5, chess.QUEEN:9, chess.KING:0}

        for sq, piece in self.board.piece_map().items():
            if piece.color == chess.WHITE:
                score += values[piece.piece_type]
            else:
                score -= values[piece.piece_type]

        centers = [chess.D4, chess.E4, chess.D5, chess.E5]
        for c in centers:
            p = self.board.piece_at(c)
            if p:
                if p.color == chess.WHITE:
                    score += 0.5
                else:
                    score -= 0.5

        white_moves = 0
        black_moves = 0
        b = self.board.copy()
        b.turn = chess.WHITE
        for _ in b.legal_moves:
            white_moves += 1
        b.turn = chess.BLACK
        for _ in b.legal_moves:
            black_moves += 1
        score += (white_moves - black_moves) * 0.1

        return score
