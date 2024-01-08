# Use Puppet to automate the task of creating a custom HTTP header response

class { 'nginx':
  ensure => 'installed',
}

file { '/etc/nginx/sites-available/default':
  ensure => present,
  content => "server {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\n\tserver_name _;\n\n\tlocation / {\n\t\tadd_header X-Served-By $hostname;\n\t\t\n\t}\n}",
}

file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
