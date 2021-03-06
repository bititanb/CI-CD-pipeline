---
layout: default
---

---

### 2020 UPDATE:
This was done back in 2017 as part of the [CI/CD demo](https://github.com/search?q=user:ilya-lesikov+topic:ci-cd-pipeline+fork:true&type=Repositories), before looking for a job as a Junior Automation Engineer. Now unmantained and left here for purely historical purposes.

---

## Что это?

{: align="justify"}
Proof-of-Concept развертывания CI/CD, приложения в нём и централизованных мониторинга и логирования. Достаточно одной машины с 5 ГБ ОЗУ, гипервизора на ней и часа времени. Развертывание полностью автоматическое.

![gh-icon-black]({{ site.baseurl }}/assets/img/github-icon-black.svg)
[**Быстрый старт с Vagrant**](https://github.com/ilya-lesikov/CI-CD-pipeline#Быстрый-старт-с-vagrantvirtualbox){: .github-link}

## Стек

| Vagrant/VirtualBox,<br>Packer/KVM | Создание VM                                     |
| Ansible                           | Развертывание инфраструктуры и приложения       |
| Jenkins                           | Сборка/тесты/деплой с Ansible[*](#ansible-note) |
| Kubernetes/Docker                 | Кластер контейнеров для приложения              |
| Django/Bootstrap                  | Приложение                                      |
| Zabbix                            | Мониторинг                                      |
| ELK                               | Логирование                                     |

## Как сделано?

Развертывание инфраструктуры и, при новых коммитах, приложения:

![]({{ site.baseurl }}/assets/img/vagrantup.plain.svg)

{: align="justify"}
Т. к. это демонстрация, некоторое сделано иначе/проще, чем должно быть. К примеру, само приложение и зависимые сервисы (БД, reverse proxy, почтовый сервер) находятся в одном [kubernetes pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/#what-is-a-pod), т.е. дублируются для каждой его реплики.  

{: align="justify"}
Где-то были и просто не очень хорошие решения, как пример — Ansible-роль вместо Groovy/shell-скриптов для сборки/тестирования (было настолько медленно, что пришлось отключить все зависимости от других ролей, а без этого Ansible не нужен). В подобных случаях, если переделывание требовало много времени, оставлял как есть, пока работает.
{: #ansible-note}

В целом, с оглядкой на то, что это демо, сделано прилично.

<div class="intrinsic-container intrinsic-container-4x3">
  <iframe marginheight="0" marginwidth="0"
  src="https://old-demo-presentation.ilya-lesikov.com" allowfullscreen></iframe>
</div>

## Как это выглядит

{: align="justify"}
4-х минутный монтаж развертывания с нуля и проверки работоспособности<br>(в реальном времени ~30-40 минут на моей машине):

<div class="intrinsic-container intrinsic-container-16x9">
  <iframe src="https://player.vimeo.com/video/240532809" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
</div>

## Далее

![gh-icon-black]({{ site.baseurl }}/assets/img/github-icon-black.svg)
[Как развернуть у себя (Windows/Linux)](https://github.com/ilya-lesikov/CI-CD-pipeline#Быстрый-старт-с-vagrantvirtualbox){: .github-link}  
![gh-icon-black]({{ site.baseurl }}/assets/img/github-icon-black.svg)
[Альтернативное развертывание с Packer/KVM (Linux)](https://github.com/ilya-lesikov/CI-CD-pipeline/tree/master/packer#Развертывание-с-packerkvm){: .github-link}

![gh-icon-black]({{ site.baseurl }}/assets/img/github-icon-black.svg)
[Основной репозиторий на GitHub](https://github.com/ilya-lesikov/CI-CD-pipeline){: .github-link}  
![gh-icon-black]({{ site.baseurl }}/assets/img/github-icon-black.svg)
[Репозиторий с Ansible](https://github.com/ilya-lesikov/ansible-taskmngr){: .github-link}  
![gh-icon-black]({{ site.baseurl }}/assets/img/github-icon-black.svg)
[Репозиторий с приложением](https://github.com/ilya-lesikov/taskmngr){: .github-link}  
![gh-icon-black]({{ site.baseurl }}/assets/img/github-icon-black.svg)
[Playbook для приложения](https://github.com/ilya-lesikov/ansible-taskmngr/tree/master/roles/taskmngr-kubernetes){: .github-link}  
