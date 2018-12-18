module Main where

import Data.List
import Data.List.Split
import Lib

main :: IO ()
main = do
    contents <- readFile "input"
    print $ sum $ map converter contents
    print $ find_basement contents

find_basement contents = length $ takeWhile (/= (-1)) $ scanl (+) 0 $ map converter contents
converter '(' = 1
converter ')' = -1
converter _ = 0

main2 = do
    contents <- readFile "input2"
    print $ sum $ map wrapping_paper $ splitOn "\n" contents

get_size [a,b,c] = 3*a*b + 2*a*c + 2*b*c
get_size _ = 0
wrapping_paper contents = get_size $ sort $ map stoi $ splitOn "x" contents
stoi s = read s ::Int
