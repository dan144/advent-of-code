module Main where

import Data.List
import Data.Sort

main :: IO ()
main = do
    contents <- readFile "input/3"
    print $ "PART ONE"
    print $ length $ Data.Sort.uniqueSort $ moves contents
    print $ "PART TWO"

moves contents = drop 1 $ scanl (sum_them) [0,0] $ map converter contents

sum_them x y = zipWith (+) x y
converter 'v' = [1,0]
converter '^' = [-1,0]
converter '<' = [0,-1]
converter '>' = [0,1]
converter _ = [0,0]
