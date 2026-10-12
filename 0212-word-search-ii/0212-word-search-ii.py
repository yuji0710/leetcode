
class Solution:
    def findWords(self, board, words):
        trie = {}

        # Step 1: Build Trie
        for word in words:
            node = trie

            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]

            node["$"] = word

        rows = len(board)
        cols = len(board[0])
        result = []

        # Step 2: DFS
        def dfs(r, c, node):
            ch = board[r][c]

            if ch not in node:
                return

            node = node[ch]

            # Step 3: Check for a complete word
            if "$" in node:
                result.append(node["$"])
                del node["$"]

            # Step 4: Backtracking
            board[r][c] = "#"

            for dr, dc in [(1, 0), (-1, 0),
                           (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    board[nr][nc] != "#"):
                    dfs(nr, nc, node)

            board[r][c] = ch

        # Step 5: Start from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return result
