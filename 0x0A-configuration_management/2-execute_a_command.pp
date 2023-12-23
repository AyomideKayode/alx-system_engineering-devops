# execute a command to kill process killmenow

exec { 'killmenow':
  path    => 'usr/bin/pkill',
  command => 'pkill -f killmenow'
}
