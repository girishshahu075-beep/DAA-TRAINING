class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = {}

        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node['$'] = word

        m, n = len(board), len(board[0])
        result = []

        def dfs(r, c, parent):

            ch = board[r][c]

            if ch not in parent:
                return

            node = parent[ch]

            if '$' in node:
                result.append(node.pop('$'))

            board[r][c] = '#'

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#':
                    dfs(nr, nc, node)

            board[r][c] = ch

            if not node:
                del parent[ch]

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie)

        return result