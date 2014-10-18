see http://chocolapod.sakura.ne.jp/blog/entry/80

easy_install coverage
easy_install nose

nosetests -v
nosetests --pdb
nosetests --with-coverage --cover-branches --cover-html
