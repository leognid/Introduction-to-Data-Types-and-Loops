boys = ['Peter', 'Alex', 'Jhon', 'Arthur', 'Richard']
girls = ['Kate', 'Liaza', 'Kira', 'Emma','Trisha' ]
if len(boys) == len(girls):
  boys.sort
  girls.sort
  couple=zip(boys,girls)  
  for date in couple:
    print(f'{date[0]} и {date[1]}')
else:
  print('не достаточное колличество людей')
  
person = int(5)
cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',  
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],  
      ]
  ]
]
for cooking in cook_book:
  for salad in cooking[1]:
    print(salad[0], salad[1] * person, salad[2])
    
