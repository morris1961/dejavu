dejavu
==========

利用[原作者](https://github.com/worldveil/dejavu)的 library 撰寫 twoSong.py，其可以比對給定的兩首歌的相似度，其原理以及結果解讀請參考原作者的說明。


## Quickstart with Docker 參考原作者，建立 docker。
First, install [Docker](https://docs.docker.com/get-docker/).

```shell
# build and then run our containers
$ docker-compose build
$ docker-compose up -d

# get a shell inside the container
$ docker-compose run python /bin/bash
Starting dejavu_db_1 ... done
root@f9ea95ce5cea:/code# python example_docker_postgres.py 
Fingerprinting channel 1/2 for test/woodward_43s.wav
Fingerprinting channel 1/2 for test/sean_secs.wav
...

# connect to the database and poke around
root@f9ea95ce5cea:/code# psql -h db -U postgres dejavu
Password for user postgres:  # type "password", as specified in the docker-compose.yml !
psql (11.7 (Debian 11.7-0+deb10u1), server 10.7)
Type "help" for help.

dejavu=# \dt
            List of relations
 Schema |     Name     | Type  |  Owner   
--------+--------------+-------+----------
 public | fingerprints | table | postgres
 public | songs        | table | postgres
(2 rows)

dejavu=# select * from fingerprints limit 5;
          hash          | song_id | offset |        date_created        |       date_modified        
------------------------+---------+--------+----------------------------+----------------------------
 \x71ffcb900d06fe642a18 |       1 |    137 | 2020-06-03 05:14:19.400153 | 2020-06-03 05:14:19.400153
 \xf731d792977330e6cc9f |       1 |    148 | 2020-06-03 05:14:19.400153 | 2020-06-03 05:14:19.400153
 \x71ff24aaeeb55d7b60c4 |       1 |    146 | 2020-06-03 05:14:19.400153 | 2020-06-03 05:14:19.400153
 \x29349c79b317d45a45a8 |       1 |    101 | 2020-06-03 05:14:19.400153 | 2020-06-03 05:14:19.400153
 \x5a052144e67d2248ccf4 |       1 |    123 | 2020-06-03 05:14:19.400153 | 2020-06-03 05:14:19.400153
(10 rows)

# then to shut it all down...
$ docker-compose down
```

If you want to be able to use the microphone with the Docker container, you'll need to do a [little extra work](https://stackoverflow.com/questions/43312975/record-sound-on-ubuntu-docker-image). I haven't had the time to write this up, but if anyone wants to make a PR, I'll happily merge.

## usage
root@f9ea95ce5cea:/code# python twoSong.py test/woodward_43s.wav test/sean_secs.wav