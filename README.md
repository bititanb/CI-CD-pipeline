
## Быстрый старт
### Windows

#### Зависимости
* Vagrant 2.0 (https://releases.hashicorp.com/vagrant/2.0.0/)
* VirtualBox 5.1 (https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* git

#### Требования
* 4.6 ГБ свободной оперативной памяти

#### Развертывание
```batch
.\scripts\hosts.bat     # от администратора, обновляет hosts

cd .\vagrant
vagrant up --provider=virtualbox
vagrant ssh taskmngr1     # пароль: 1
sudo ansible-playbook /etc/ansible/taskmngr.yaml
```

После того, как Ansible завершит работу, за сборкой, тестированием и развертыванием приложения в кластере Kubernetes можно наблюдать в Jenkins (http://taskmngr1:8080/job/taskmngr).

По окончанию будут доступны:
| Сервис | Адрес | Пользователь | Пароль |
| - | - | - | - |
| Приложение (production) | [taskmngr1](https://taskmngr1) | - | - |
| Приложение (testing) | [testing.taskmngr1](http://testing.taskmngr1) | - | - |
| Zabbix | [taskmngr1:8088](http://taskmngr1:8088) | Admin | zabbix |
| Kibana | [taskmngr1:8085](http://taskmngr1:8085/app/kibana#/settings/indices/filebeat-*?_g=%28time:%28from:now-24h%29%29)<br>(нажмите <img src="./res/defaultindexbutton.png" height="20px"/> и *Discover* для логов) | - | - |
| Jenkins | [taskmngr1:8080](http://taskmngr1:8080/job/taskmngr) | admin | admin |
