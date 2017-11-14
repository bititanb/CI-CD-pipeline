---
layout: default
---

## Что это?

{: align="justify"}
Proof-of-Concept развертывания CI/CD, приложения в нём и централизованных мониторинга и логирования. Развертывание полностью автоматическое.

[Быстрый старт с Vagrant](https://github.com/bititanb/CI-CD-pipeline#Быстрый-старт-с-vagrantvirtualbox)

## Стек

| Vagrant/VirtualBox или Packer/KVM | Создание VM                                     |
| Ansible                           | Развертывание инфраструктуры и приложения       |
| Jenkins                           | Сборка/тесты/деплой с Ansible[*](#ansible-note) |
| Kubernetes/Docker                 | Кластер контейнеров для приложения              |
| Django/Bootstrap/Postgres/Nginx   | Приложение                                      |
| Zabbix                            | Мониторинг                                      |

*Подобран просто по распространенности.*

## Как сделано?

Развертывание инфраструктуры и, при новых коммитах, приложения:

![]({{ site.baseurl }}/assets/img/vagrantup.plain.svg)

{: align="justify"}
Т. к. это демонстрация, некоторое сделано иначе/проще, чем должно быть. К примеру, само приложение и зависимые сервисы (БД, reverse proxy, почтовый сервер) находятся в одном [kubernetes pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/#what-is-a-pod), т.е. дублируются для каждой его реплики, притом БД контейнеризованы (что для боевых условий не годится).  

{: align="justify"}
Иногда были и просто плохие решения, как пример — Ansible-роль вместо Groovy/shell-скриптов для сборки/тестирования (было настолько медленно, что пришлось отключить все зависимости от других ролей, а без этого Ansible не нужен). В подобных случаях, если переделывание требовало много времени, оставлял как есть, пока работает.
{: #ansible-note}

В целом, с оглядкой на то, что это демо, сделано прилично.

<div class="intrinsic-container intrinsic-container-4x3">
  <iframe marginheight="0" marginwidth="0" src="https://bititanb.github.io/CI-CD-pipeline-presentation" allowfullscreen></iframe>
</div>

## Как это выглядит

{: align="justify"}
4-х минутный монтаж развертывания с нуля и проверки работоспособности (в реальном времени ~30-40 минут на моей машине):

<div class="intrinsic-container intrinsic-container-16x9">
  <iframe src="https://player.vimeo.com/video/240532809" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
</div>

## Далее

[Как развернуть у себя (Windows/Linux)](https://github.com/bititanb/CI-CD-pipeline#Быстрый-старт-с-vagrantvirtualbox)  
[Альтернативное развертывание с Packer/KVM (Linux)](https://github.com/bititanb/CI-CD-pipeline/tree/master/packer#Развертывание-с-packerkvm)

[Основной репозиторий](https://github.com/bititanb/CI-CD-pipeline)  
[Репозиторий с Ansible](https://github.com/bititanb/ansible-taskmngr)  
[Репозиторий с приложением](https://github.com/bititanb/taskmngr)  
[Playbook для приложения](https://github.com/bititanb/ansible-taskmngr/tree/master/roles/taskmngr-kubernetes)  
