class Solution:
    def floodFill(self, image: list,
                  sr: int, sc: int,
                  color: int) -> list:

        original = image[sr][sc]

        # if already same color → no change!
        if original == color:
            return image

        def dfs(r, c):
            if r<0 or r>=len(image):
                return
            if c<0 or c>=len(image[0]):
                return
            if image[r][c] != original:
                return

            image[r][c] = color    # fill!

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)
        return image
