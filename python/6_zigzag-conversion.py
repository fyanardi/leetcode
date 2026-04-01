class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 0:
            return s

        if numRows == 1:
            return s

        # E.g: Input: s = "PAYPALISHIRING", numRows = 4
        #      Output: "PINALSIGYAHRPI"
        #   | 0 1 2 3 4 5 6
        # ---------------
        # 0 | P     L     N
        # 1 | A   L I   I G
        # 2 | Y A   H R
        # 3 | P     J

        # c represents the number of characters per "full cycle"
        # "full cycle" is defined as 1 column with the vertical pattern occupying all rows (e.g: column 0 "PAYP")
        # and all diagonal characters that are not part of the vertical pattern (e.g. column 1 'A' and column 2 'L')
        c = numRows * 2 - 2

        # calculate the number of columns
        numCols = (
            # number of "full cycle" times total columns per full cycle (numRows - 1)
            int(len(s) / c) * (numRows - 1)
            # whether there is any vertical pattern for the last, non-full cycle
            + int(len(s) % c / numRows)
            # remaining of the diagonal characters for the last, non-full cycle
            + len(s) % c % numRows
        )

        # output in 2D array, each element initialized with ' '
        output = [
            [' ' for _ in range(numCols)]
            for _ in range(numRows)
        ]

        for i in range(len(s)):
            if i % c < numRows:
                x = int(i / c) * (numRows - 1)
                y = i % c
            else:
                x = int(i / c) * (numRows - 1) + (i % c) - numRows + 1
                y = c - (i % c)

            output[y][x] = s[i]

        # pretty print the output
        # for i in range(len(output)):
        #     print(output[i])

        return ''.join([''.join([c.strip() for c in row]).strip() for row in output])


if __name__ == "__main__":
    solution = Solution()

    print(solution.convert("PAYPALISHIRING", 3))
    print(solution.convert("PAYPALISHIRING", 4))
    print(solution.convert("A", 1))
    print(solution.convert("A", 2))
    print(solution.convert("AB", 1))
    print(solution.convert("twttvdpljlfvnpuwdxsabnheyrwdpqdimyejbtvnhciwucuzbnzfcgldyjgpzlzojdzlzwyizievmbuoquvsagxapdprqrhaugntdnbevibhjvxzpstsarsswkjpdsrxyetdrwjogkxpgxqxrmpsfkmdwxszpjynnrtgoewupwmxteukqmevwqbsnttcdrssjnbzrzvivjfoqcbgofemwfglazodsiydvbemacvylcobepkuxqivxogxpwdieblzeqogsjeflvjskvojlxginnfdlknqlarrqfykoesczbwmwmvjjcrzryecjruwrmqkrowisomurignwdyihrhasldbczzvlpfffcpasbuklczhfypppwphjuknumjhbqmhsbjncdxphwxmwodoltvwnikjutrxjfgehprluqdbmaqlotzbowyeeknadgyomeuvwniqdlsslidcbcfsafwfpjhuqfjemfzithawtsqgatkexqwyxufndohvwsbiyastksrdnilpdytdqrdnnkarykoueqeeswxcrphezvtctphjikywuzptlfprxuwqstujkeplzjquaxfiidgeevzrdpjajfsbapnltcyuloqnmvywaeafccyfrhhamcdprqamtaigpywdvuzxabecddjwktwzvcomuqanqiwhiskdojconhtskcpwxnvsplgkbgzuoxbwpmbfxeumnnfzruvphthxeojiwiclgfjxtndrtzdgmiffccumvejcuukqeodktnkpcpgvoldawkfamcmigxmcrwswmwihluwnjeixslzoxhojjdtrcftudnsrjczwxxjgctgugfkdmanxdgqiolc", 525))
    print(solution.convert("wjkakhxhsglmmhstrwgulfztwhhjlbihmviwehfwntibadvubdomiphgxpsiscsexccbjhazakadnvxqanelemtbdlmvoezlgbprkpqlbtqpqphrcmcgyvkbhwyvcxikazbkquxsnpjdeqwicyrcwbfdzdabcklcmmpciouvedbiwxryyidulizkmblonwtzkkcvayqectpariyrqdldmmnynaoawjaivedwcwcgrrgibhbtkmwwyjwnjnohyqsuuxqwvufnmlxnszhfnfbmpabaprknhchdzzaxufkishxngeswkvkbvlbkdlamphqrhsodzylrhieqpymbuwcrhfemtezklpbuhrxgpkzzvgpkedlyzpqiwuvrywelnfguxfcosdpnjexohkoiberzaotymxmzeuvdbzutcjimqhcxrqiuxbwxrpydokcsgxwhwqdazloptqpmjzjgafftwdwkpacxzafxqkxsvmjqeadpbmvbtbupgsbysdvtecqwmqqiecaicdyervhkyebhwcfricmofdmttddxfehjhhnbdxnbbpiztpsdufrzkeudjycqcjzltpmwmczprkqmblqvqjwcnrfypjotuoenftlrvlioxycylsubcqfrhksyvgrqwyfbtruqecgbdibodvshoxaxksyhbrxxrfbkyvccaifftgtwendulfrxyrebjeaajbljzplzyseryzpenuyazszxldyujzvucidbxqcxiiqjifnxbozbiyatdzqpaljevpisfksovkxfqmctcdumdviiwyxwljcgykadvsrsdqxvfbojelwjgercerapacvypxdmqxevpbsucieitctbikdmdfdfkydzvjlngpkvqcsunyeiaxkijnwnvzsfzyewhpkpewmwbeqocwwetgmcwkrrjkwikahtrtivpurqbjgffdkalwcjjuasgydqamjrftmupfnqqtwxyixmgavp", 621))
