Objective
===========
Practice the command line by munging datasets using just the command line.

Transforming data sets to make them easier to work with.

Data Sets
===========
The data sets come from U.S. Housing affordability from the [U.S. Department of Housing & Urban Development](http://www.huduser.org/portal/datasets/hads/hads.html)

The data sets contains 3 files : Hud_2005.csv, Hud_2007.csv, Hud_2013.csv

Data Munging
============

Display all files in the current directory:

    $ ls
    Hud_2005.csv  Hud_2007.csv  Hud_2013.csv

Data Exploration
================

Display the first 5 rows from the file:

    $ head Hud_2005.csv

      1 CONTROL         AGE1  BEDRMS  PER  REGION  LMED    FMR   L30    L50    L80     IPOV   BUILT  STATUS  VACANCY  TENURE  NUNITS  TYPE  VALUE    ZINC2    ROOMS  ZADEQ  ZSMHC  WEIGHT        METRO3  STRUCTURETYPE  OWNRENT  UTILITY       OTHERCOST     COST06        COST
      2 '100006110249'  43    3       1    '3'     47954   680   10359  17263  27615   9930   1980   '1'     -6       '1'     1       1     90000    20000    8      '1'    855    2916.5267516  '5'     1              '1'      160.16666667  33.333333333  791.63592537  1139
      3 '100006370140'  44    4       5    '3'     47954   760   15988  26630  42607   23742  1985   '1'     -6       '1'     1       1     150000   71000    8      '1'    1317   2457.9881717  '5'     1              '1'      117           62.5          1176.393209   1755
      4 '100006520140'  58    3       3    '3'     47954   680   13321  22194  35506   15364  1985   '1'     -6       '1'     1       1     187000   64729    6      '1'    1175   2454.8734738  '5'     1              '1'      135           61.75         1439.5435338  2161
      5 '100007130148'  22    1       1    '3'     56785   519   12104  20182  32291   9974   1980   '1'     -6       '2'     16      1     -6       27040    3      '2'    490    3543.6903963  '1'     3              '2'      64.75         0             490           490

    $ head Hud_2007.csv
    
      1 CONTROL         AGE1  BEDRMS  PER  REGION  LMED    FMR   L30    L50    L80     IPOV   BUILT  STATUS  TYPE  VALUE    VACANCY  TENURE  NUNITS  ZINC2    ROOMS  ZADEQ  ZSMHC  WEIGHT        METRO3  STRUCTURETYPE  OWNRENT  UTILITY       OTHERCOST     COST06        COST
      2 '100003130103'  -9    3       -6   '1'     66440   1048  14344  23890  37385   -6     2006   '3'     1     140000   3        '-6'    1       -6       5      '-6'   -6     2452.2148835  '3'     1              '1'      0             0             930.43366169  1471
      3 '100003130203'  69    3       1    '1'     66440   1048  14344  23890  37385   9810   2006   '1'     1     250      -6       '1'     1       47400    5      '1'    477    3769.2680331  '3'     1              '1'      296.5         15.083333333  313.24482201  314.
      4 '100006110249'  45    3       1    '3'     49575   757   10893  18140  29019   10573  1980   '1'     1     130000   -6       '1'     1       26000    6      '1'    798    2420.5321313  '5'     1              '1'      131.66666667  37.5          1033.1407811  1535
      5 '100006370140'  47    4       5    '3'     49575   847   16793  27980  44774   25442  1985   '1'     1     300000   -6       '1'     1       174050   7      '1'    1442   2654.7464687  '5'     1              '1'      134           75            2202.7864179  3361
    
    
    $ head Hud_2013.csv
    
      1 CONTROL         AGE1  METRO3  REGION  LMED    FMR   L30    L50    L80     IPOV   BEDRMS  BUILT  STATUS  TYPE  VALUE    VACANCY  TENURE  NUNITS  ROOMS  WEIGHT        PER  ZINC2    ZADEQ  ZSMHC  STRUCTURETYPE  OWNRENT  UTILITY       OTHERCOST     COST06        COST
      2 '100003130103'  82    '3'     '1'     73738   956   15738  26213  40322   11067  2       2006   '1'     1     40000    -6       '1'     1       6      3117.394239   1    18021    '1'    533    1              '1'      169           213.75        648.58818905  803.
      3 '100006110249'  50    '5'     '3'     55846   1100  17165  28604  45744   24218  4       1980   '1'     1     130000   -6       '1'     1       6      2150.7255443  4    122961   '1'    487    1              '1'      245.33333333  58.333333333  1167.6407811  1669
      4 '100006370140'  53    '5'     '3'     55846   1100  13750  22897  36614   15470  4       1985   '1'     1     150000   -6       '1'     1       7      2213.7894038  2    27974    '1'    1405   1              '1'      159           37.5          1193.393209   1772
      5 '100006520140'  67    '5'     '3'     55846   949   13750  22897  36614   13964  3       1985   '1'     1     200000   -6       '1'     1       6      2364.585097   2    32220    '1'    279    1              '1'      179           70.666666667  1578.8576119  2351
      
      
Consolidating Data sets
=======================

Create new file that contains of the 3 files:

    $ head -1 Hud_2005.csv > combined_hud.csv
    $ wc -l Hud_2005.csv
    46854 Hud_2005.csv
    $ wc -l Hud_2007.csv
    42730 Hud_2007.csv
    $ wc -l Hud_2013.csv
    64536 Hud_2013.csv
    $ tail -46853 Hud_2005.csv >> combined_hud.csv
    $ tail -42729 Hud_2007.csv >> combined_hud.csv
    $ tail -64535 Hud_2013.csv >> combined_hud.csv
    $ head combined_hud.csv
      1 CONTROL         AGE1  BEDRMS  PER  REGION  LMED    FMR    L30    L50     L80     IPOV   BUILT  STATUS  VACANCY  TENURE   NUNITS  TYPE  VALUE    ZINC2    ROOMS         ZADEQ  ZSMHC    WEIGHT        METRO3  STRUCTURETYPE  OWNRENT  UTILITY       OTHERCOST     COST06
      2 '100006110249'  43    3       1    '3'     47954   680    10359  17263   27615   9930   1980   '1'     -6       '1'      1       1     90000    20000    8             '1'    855      2916.5267516  '5'     1              '1'      160.16666667  33.333333333  791.63
      3 '100006370140'  44    4       5    '3'     47954   760    15988  26630   42607   23742  1985   '1'     -6       '1'      1       1     150000   71000    8             '1'    1317     2457.9881717  '5'     1              '1'      117           62.5          1176.3
      4 '100006520140'  58    3       3    '3'     47954   680    13321  22194   35506   15364  1985   '1'     -6       '1'      1       1     187000   64729    6             '1'    1175     2454.8734738  '5'     1              '1'      135           61.75         1439.5
      5 '100007130148'  22    1       1    '3'     56785   519    12104  20182   32291   9974   1980   '1'     -6       '2'      16      1     -6       27040    3             '2'    490      3543.6903963  '1'     3              '2'      64.75         0             490


Counting
=========

Count and display the number of lines in combined_hud.csv containing 1980-1989.

    $ grep '1980-1989' combined_hud.csv | wc -l
    19711

