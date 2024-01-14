# nginx_setup.pp

package { 'nginx':
  ensure => installed,
}

file { '/data':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
}

file { '/data/web_static':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
}

file { '/data/web_static/releases':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
}

file { '/data/web_static/shared':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
}

file { '/data/web_static/releases/test':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => '<html><head><title>Test Page</title></head><body>Hello, this is a test page!</body></html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test/',
  force   => true,
}

file_line { 'nginx_config':
  path   => '/etc/nginx/sites-available/default',
  line   => '  location /hbnb_static/ {',
  match  => '^server {',
  after  => '  }',
  notify => Service['nginx'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File_line['nginx_config'],
}
