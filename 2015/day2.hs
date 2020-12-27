module Main where

import Data.List
import Data.List.Split

main :: IO ()
main = do
    contents <- readFile "input/2"
    print $ "PART ONE"
    print $ sum $ map wrapping_paper $ splitOn "\n" contents
    print $ "PART TWO"
    print $ sum $ map ribbon $ splitOn "\n" contents

get_size [a,b,c] = 3*a*b + 2*a*c + 2*b*c
get_size _ = 0
get_ribbon [a,b,c] = 2*(a+b) + a*b*c
get_ribbon _ = 0
wrapping_paper contents = get_size $ sort $ map stoi $ splitOn "x" contents
ribbon contents = get_ribbon $ sort $ map stoi $ splitOn "x" contents
stoi s = read s ::Int
