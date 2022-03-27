def parser(file_name):
  headers = ["number of jobs", "number of machines", "initial seed", "upper bound and lower bound"]
  
  dic = {}
  items = []
  next_h = False
  first = True

  with open(file_name) as file:
    for line in file:
      formated_line = line.strip()

      if formated_line.startswith('number of jobs'):
        if first:
          first = False
        else:
          items.append(dic)

        dic = {}
        dic['processing'] = []
        next_h = True
      elif next_h:
        next_h = False
        splitted = formated_line.split()

        for header in range(len(headers)):
          dic[headers[header]] = int(splitted[header])
      elif not formated_line.startswith('processing'):
        num = list(map(lambda x: int(x), formated_line.split()))
        dic['processing'].append(num)
  return items


def parse_files(files):
  return list(map(lambda x : parser(x)[0], files))
