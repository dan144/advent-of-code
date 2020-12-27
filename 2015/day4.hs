module Main where

import Data.Digest.Pure.MD5
import qualified Data.ByteString.Lazy as B
import Data.ByteString
import Data.ByteString.Conversion.To

main :: IO ()
main = do
    contents <- B.readFile "input/4"
    print $ "PART ONE"
    print $ get_index $ map_hash $ map_num (B.init contents)
    print $ "PART TWO"
    print $ get_extra_index $ map_hash $ map_num (B.init contents)

add_num s n = B.concat [s, toByteString n]
add_num _ _ = toByteString ""

map_num s = Prelude.map (add_num s) [1 :: Integer ..]
get_hash value = show $ md5 value
map_hash vs = Prelude.map get_hash vs

is_not_valid ('0':'0':'0':'0':'0':xs) = False
is_not_valid _ = True

is_not_extra_valid ('0':'0':'0':'0':'0':'0':xs) = False
is_not_extra_valid _ = True

get_index hashes = (\x -> x +1) $ Prelude.length $ Prelude.takeWhile (is_not_valid) hashes
get_extra_index hashes = (\x -> x +1) $ Prelude.length $ Prelude.takeWhile (is_not_extra_valid) hashes
