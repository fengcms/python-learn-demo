const shuffle = (array) => {
  let res = [], random;
  while(array.length>0){
    random = Math.floor(Math.random()*array.length);
    res.push(array[random]);
    array.splice(random, 1);
  }
  return res;
}

const randint = (min, max) => {
  const range = max - min
  const rand = Math.random()
  return (min + Math.round(rand * range))
}

const choice = (str) => {
  const i = ~~(Math.random() * str.length)
  return str[i]
}

module.exports = {
  shuffle, randint, choice
}
