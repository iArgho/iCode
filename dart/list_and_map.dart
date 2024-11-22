void main() {
  var list = [1, 2, 3, 4];
  var map = {
    'a': 'b',
    'c': 'd',
  };
  print(list[0]);
  print(map['a']);

  list.add(5);
  print(list);
  list[2] = 0;
  print(list);
}
