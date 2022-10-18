#!/usr/bin/pup
# kills process 'killmenow'
exec {'pkill'
    command => 'pkill killmenow',
    provider => 'server'
}