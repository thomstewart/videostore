#!/usr/bin/bash

import sqlite3

ITEM_TYPE ITEM_TITLE                                                   ITEM_RAT
---------- ------------------------------------------------------------ --------
      1014 Pirates of the Caribbean - The Curse of the Black Pearl      PG-13
      1014 Pirates of the Caribbean - The Curse of the Black Pearl      PG-13
      1013 Pirates of the Caribbean - The Curse of the Black Pearl      PG-13
      1014 Pirates of the Caribbean - Dead Man's Chest                  PG-13
      1014 Pirates of the Caribbean - Dead Man's Chest                  PG-13
      1014 Pirates of the Caribbean - At World's End                    PG-13
      1014 Pirates of the Caribbean - At World's End                    PG-13
      1014 Indiana Jones and the Raiders of the Lost Ark                PG
      1013 Indiana Jones and the Raiders of the Lost Ark                PG
      1014 Indiana Jones and the Temple of Doom                         PG
      1013 Indiana Jones and the Temple of Doom                         PG
      1014 Indiana Jones and the Last Crusade                           PG-13
      1013 Indiana Jones and the Last Crusade                           PG-13
      1014 Spider-Man                                                   PG-13
      1013 Spider-Man                                                   PG-13
      1014 Spider-Man 2                                                 PG-13
      1013 Spider-Man 2                                                 PG-13
      1014 Spider-Man 3                                                 PG-13
      1013 Spider-Man 3                                                 PG-13
      1014 Star Wars - Episode I                                        PG
      1014 Star Wars - Episode II                                       PG
      1013 Star Wars - Episode II                                       PG
      1014 Star Wars - Episode III                                      PG-13
      1013 Star Wars - Episode III                                      PG-13
      1014 Star Wars - Episode IV                                       PG
      1013 Star Wars - Episode IV                                       PG
      1014 Star Wars - Episode V                                        PG
      1013 Star Wars - Episode V                                        PG
      1014 Star Wars - Episode VI                                       PG
      1013 Star Wars - Episode VI                                       PG
      1014 The Sum of All Fears                                         PG-13
      1014 The Patriot                                                  R
      1014 The Patriot                                                  NR
      1014 We Were Soldiers                                             R
      1014 Chronicles of Narnia - The Lion, the Witch and the Wardrobe  PG
      1013 Chronicles of Narnia - The Lion, the Witch and the Wardrobe  PG
      1015 Chronicles of Narnia - The Lion, the Witch and the Wardrobe  T
      1016 Chronicles of Narnia - The Lion, the Witch and the Wardrobe  T
      1017 Chronicles of Narnia - The Lion, the Witch and the Wardrobe  T
      1015 Harry Potter: Goblet of Fire                                 E10+
      1016 Harry Potter: Goblet of Fire                                 E10+
      1017 Harry Potter: Goblet of Fire                                 E10+
      1015 Pirates of the Caribbean                                     T
      1016 Pirates of the Caribbean                                     T
      1017 Pirates of the Caribbean                                     T
      1017 Pirates of the Caribbean                                     T
      1014 Around the World in 80 Days                                  NR
      1014 Around the World in 80 Days                                  PG
      1014 Casino Royale                                                PG-13
      1013 Casino Royale                                                PG-13
      1014 Die Another Day                                              PG-13
      1014 Die Another Day                                              PG-13
      1013 Die Another Day                                              PG-13
      1014 Golden Eye                                                   PG-13
      1014 Golden Eye                                                   PG-13
      1014 Tomorrow Never Dies                                          PG-13
      1014 Tomorrow Never Dies                                          PG-13
      1014 The World Is Not Enough                                      PG-13
      1014 The World Is Not Enough                                      PG-13
      1014 Brave Heart                                                  R
      1014 Camelot                                                      G
      1013 Christmas Carol                                              NR
      1013 Christmas Carol                                              PG
      1014 Scrooge                                                      G
      1014 Clear and Present Danger                                     PG-13
      1014 Clear and Present Danger                                     PG-13
      1014 Harry Potter and the Sorcer's Stone                          PG
      1013 Harry Potter and the Sorcer's Stone                          PG
      1014 Harry Potter and the Chamber of Secrets                      PG
      1013 Harry Potter and the Chamber of Secrets                      PG
      1014 Harry Potter and the Prisoner of Azkaban                     PG
      1013 Harry Potter and the Prisoner of Azkaban                     PG
      1014 Harry Potter and the Chamber of Secrets                      PG
      1014 Harry Potter and the Goblet of Fire                          PG-13
      1013 Harry Potter and the Goblet of Fire                          PG-13
      1013 Harry Potter and the Goblet of Fire                          PG-13
      1014 Harry Potter and the Order of the Phoenix                    PG-13
      1014 The Hunt for Red October                                     PG
      1014 The Hunt for Red October                                     PG
      1014 King Arthur - The Director's Cut                             R
      1013 King Arthur                                                  PG-13
      1014 King Arthur - The Director's Cut                             R
      1014 The Lord of the Rings - Fellowship of the Ring               PG-13
      1013 The Lord of the Rings - Fellowship of the Ring               PG-13
      1014 The Lord of the Rings - Fellowship of the Ring               PG-13
      1014 The Lord of the Rings - Two Towers                           PG-13
      1013 The Lord of the Rings - Two Towers                           PG-13
      1014 The Lord of the Rings - Two Towers                           PG-13
      1014 The Lord of the Rings - The Return of the King               PG-13
      1013 The Lord of the Rings - The Return of the King               PG-13
      1014 The Lord of the Rings - The Return of the King               PG-13
      1014 The Patriot Games                                            R
      1014 The Patriot Games                                            R


