import yaml
if __name__ == '__main__':
 with open('./user.yml', 'r') as file:
     data = yaml.safe_load(file)
 user=data['user']    
 print(user['name'])    
 for role in user['roles']:
     print(role)
 user['location']['city']='PUEBLA'
 with open('Rosario.yml', 'w') as file:
     yaml.dump(data,file, default_flow_style=False)
