module Main where

import Data.List
import Data.Sort

main :: IO ()
main = do
    contents <- readFile "input/3"
    print $ "PART ONE"
    print $ length $ Data.Sort.uniqueSort $ locations contents
    print $ "PART TWO"
    let santa_moves = every_other contents
    let robo_moves = every_other $ drop 1 contents

    print $ length $ Data.Sort.uniqueSort $ (locations santa_moves ++ locations robo_moves)

locations contents = drop 1 $ scanl (sum_them) [0,0] $ map converter contents

every_other (x:y:xs) = x : every_other xs
every_other _ = []

sum_them x y = zipWith (+) x y

converter 'v' = [1,0]
converter '^' = [-1,0]
converter '<' = [0,-1]
converter '>' = [0,1]
converter _ = [0,0]
