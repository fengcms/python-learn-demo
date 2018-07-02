for i in $(cat imgOldUrlBak.txt); do
  curl -O $i;
  sleep 1;
done
