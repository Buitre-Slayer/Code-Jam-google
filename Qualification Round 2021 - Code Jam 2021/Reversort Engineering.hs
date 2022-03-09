import Control.Monad

minCost n = n - 1

maxCost n = ((n * (n + 1)) / 2) - 1

impossible n c = c < minCost n || c > maxCost n

getReversePositions 1 _ = [0]
getReversePositions n c = 
    pos : getReversePositions (n-1) (c-pos)
    where pos = minimum [n, c-(n-2)]

getSequence [] y = tail y
getSequence (x:xs) y = 
    getSequence xs (length xs : reverse(take x y) ++ reverse(take (length y - x) (reverse y)))

main = do
    nTests <- getLine
    forM_ [1..read nTests :: Int] (\a ->do
        paramsImpure <- getLine
        let paramsList = map read $ words paramsImpure :: [Int]
        let n = head paramsList
        let c = last paramsList
        let reversePositions = tail $ reverse (getReversePositions n c)
        let sequence = getSequence reversePositions [n-1, n]
        let sequenceString = unwords $ map show sequence
        if impossible (fromIntegral n) (fromIntegral c) then
            putStrLn ("Case #" ++ show a ++ ": IMPOSSIBLE")
        else
            putStrLn ("Case #" ++ show a ++ ": " ++ sequenceString)
        return ()
        )
    