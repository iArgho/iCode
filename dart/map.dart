void main() {
  var stu = {1: 'Argho', 2: 'Roy'};
  stu[3] = 'Anupam';
  print(stu);

  // Map using constructor
  var phone = new Map();

  phone['Model'] = '14 Pro';
  phone['Ram'] = 6;

  print(phone);

  phone.addAll({
    'Display': 'XDR',
  });

  print(phone);
}
