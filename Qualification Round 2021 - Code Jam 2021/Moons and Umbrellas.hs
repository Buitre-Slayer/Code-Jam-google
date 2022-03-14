{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use head" #-}
{-# OPTIONS_GHC -Wno-incomplete-patterns #-}

import Control.Monad

readInt :: IO Int
readInt = readLn

getP [] = 0
getP (x:xs) = if x == '?' then getP xs + 1 else 0

getLastLiteral (x:xs) = if x /= '?' then x else getLastLiteral xs

calculateCost x y 'C' 'J' = x
calculateCost x y 'J' 'C' = y
calculateCost x y a b = 0

solution x y [a] = 0
solution x y ('C':'J':xs) = x + solution x y ('J' : xs)
solution x y ('J':'C':xs) = y + solution x y ('C' : xs)
solution x y ('?':b:xs) = solution x y (b:xs)
solution x y (a:'?':xs) =
    minimum l + solution x y ('?':xs)
    where
        lastLiteral = getLastLiteral xs
        p = getP $ '?':xs
        halfP = div p 2 :: Int
        penultimateStartC = if even p then 'J' else 'C'
        penultimateStartJ = if even p then 'C' else 'J'
        s1 = [calculateCost x y a 'C' + calculateCost x y 'C' lastLiteral
             ,
             calculateCost x y a 'J' + calculateCost x y 'J' lastLiteral]
        s2 = [calculateCost x y a 'C' + calculateCost x y penultimateStartC lastLiteral +
             halfP * x + (halfP - mod (p + 1) 2) * y
             ,
             calculateCost x y a 'J' + calculateCost x y penultimateStartJ lastLiteral +
             halfP * y + (halfP - mod (p + 1) 2) * x]
        s3 = [calculateCost x y a 'C' + calculateCost x y penultimateStartJ lastLiteral +
             (halfP - mod (p + 1) 2) * x + (halfP - 1) * y
             ,
             calculateCost x y a 'J' + calculateCost x y penultimateStartC lastLiteral +
             (halfP - mod (p + 1) 2) * y + (halfP - 1) * x]
        l | p == 1 =
            s1
          | p == 2 =
              s1 ++ s2
          | otherwise =
              s1 ++ s2 ++ s3
solution x y (a:b:xs) = solution x y (b:xs)


main = do
    nTestCases <- readInt
    forM_ [1 .. nTestCases] (\a -> do
        parameters <- getLine
        let parametersList = words parameters
        let x = read $ parametersList!!0 :: Int
        let y = read $ parametersList!!1 :: Int
        let s = 'x' : parametersList!!2 ++ ['x']
        putStrLn ("Case #" ++ show a ++ ": " ++ show (solution x y s))
        return ()
        )
    