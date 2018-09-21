#!/bin/bash

#today=`date +%Y-%m-%d-%H-%M-%S`

#for i in {1..6};
for i in {1};
do
today=`date +%Y-%m-%d-%H-%M-%S`

(cat $today'.html'| wget -O - http://wsj.com/mdc/public/page/2_3021-activnyse-actives.html | egrep -o '.*' > $today'.html') && (sleep 1)
#(cat $today'.html'| wget -O - http://wsj.com/mdc/public/page/2_3021-activnyse-actives.html | egrep -o '.*' > $today'.html')


java -jar tagsoup-1.2.1.jar --files $today'.html'


python hhw7.py $today'.xhtml' $today'.csv' >$today'.csv'

done