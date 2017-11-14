---
layout: default
---

## Что это?

{: align="justify"}
Proof-of-Concept развертывания CI/CD, приложения в нём и централизованных мониторинга и логирования. Развертывание полностью автоматическое.

[Быстрый старт с Vagrant](https://github.com/bititanb/CI-CD-pipeline#Быстрый-старт-с-vagrantvirtualbox)

## Стек
> Подобран просто по распространенности.

| Vagrant/VirtualBox или Packer/KVM | Создание VM                                     |
| Ansible                           | Развертывание инфраструктуры и приложения       |
| Jenkins                           | Сборка/тесты/деплой с Ansible[*](#ansible-note) |
| Kubernetes/Docker                 | Кластер контейнеров для приложения              |
| Django/Bootstrap/Postgres/Nginx   | Приложение                                      |
| Zabbix                            | Мониторинг                                      |
| ELK/Filebeat                      | Логирование                                     |


## Как сделано?

Развертывание инфраструктуры и, при новых коммитах, приложения:

![]({{ site.baseurl }}/assets/img/vagrantup.plain.svg)

{: align="justify"}
Т. к. это демонстрация, некоторое сделано иначе/проще, чем должно быть. К примеру, само приложение и зависимые сервисы (БД, reverse proxy, почтовый сервер) находятся в одном [kubernetes pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/#what-is-a-pod), т.е. дублируются для каждой его реплики, притом БД контейнеризованы (что для боевых условий не годится).  

{: align="justify"}
Иногда были и просто плохие решения, как пример — Ansible-роль вместо Groovy/shell-скриптов для сборки/тестирования/деплоя (было настолько медленно, что пришлось отключить все зависимости от других ролей, а без этого Ansible не нужен). В подобных случаях, если переделывание требовало много времени, оставлял как есть, пока работает.
{: #ansible-note}

В целом, с оглядкой на то, что это демо, сделано прилично.

<div class="intrinsic-container intrinsic-container-4x3">
  <iframe marginheight="0" marginwidth="0" src="https://bititanb.github.io/CI-CD-pipeline-presentation" allowfullscreen></iframe>
  <!-- <iframe marginheight="0" marginwidth="0" src="http://localhost:8000" allowfullscreen></iframe> -->
</div>
<!-- <iframe width="960" height="740" marginheight="0" marginwidth="0" src="http://localhost:8000"></iframe> -->

## Как это выглядит

{: align="justify"}
4-х минутный монтаж развертывания с нуля и проверки работоспособности (в реальном времени ~30-40 минут на моей машине):

<div class="intrinsic-container intrinsic-container-16x9">
  <iframe src="https://player.vimeo.com/video/240532809" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
</div>
<!-- <iframe src="https://player.vimeo.com/video/240532809" width="960" height="540" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> -->

## Далее

[Как развернуть у себя (Windows/Linux)](https://github.com/bititanb/CI-CD-pipeline#Быстрый-старт-с-vagrantvirtualbox)  
[Альтернативное развертывание с Packer/KVM (Linux)](https://github.com/bititanb/CI-CD-pipeline/tree/master/packer#Развертывание-с-packerkvm)

[Основной репозиторий](https://github.com/bititanb/CI-CD-pipeline)  
[Репозиторий с Ansible](https://github.com/bititanb/ansible-taskmngr)  
[Репозиторий с приложением](https://github.com/bititanb/taskmngr)  
[Playbook для приложения](https://github.com/bititanb/ansible-taskmngr/tree/master/roles/taskmngr-kubernetes)  
















<!---
Text can be **bold**, _italic_, or ~~strikethrough~~.


[Link to another page](another-page).

There should be whitespace between paragraphs.

There should be whitespace between paragraphs. We recommend including a README, or a file with information about your project.

# [](#header-1)Header 1

This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

## [](#header-2)Header 2

> This is a blockquote following a header.
>
> When something is important enough, you do it even if the odds are not in your favor.

### [](#header-3)Header 3

```js
// Javascript code with syntax highlighting.
var fun = function lang(l) {
  dateformat.i18n = require('./lang/' + l)
  return true;
}
```

```ruby
# Ruby code with syntax highlighting
GitHubPages::Dependencies.gems.each do |gem, version|
  s.add_dependency(gem, "= #{version}")
end
```

#### [](#header-4)Header 4

*   This is an unordered list following a header.
*   This is an unordered list following a header.
*   This is an unordered list following a header.

##### [](#header-5)Header 5

1.  This is an ordered list following a header.
2.  This is an ordered list following a header.
3.  This is an ordered list following a header.

###### [](#header-6)Header 6

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

### There's a horizontal rule below this.

* * *

### Here is an unordered list:

*   Item foo
*   Item bar
*   Item baz
*   Item zip

### And an ordered list:

1.  Item one
1.  Item two
1.  Item three
1.  Item four

### And a nested list:

- level 1 item
  - level 2 item
  - level 2 item
    - level 3 item
    - level 3 item
- level 1 item
  - level 2 item
  - level 2 item
  - level 2 item
- level 1 item
  - level 2 item
  - level 2 item
- level 1 item

### Small image

![](https://assets-cdn.github.com/images/icons/emoji/octocat.png)

### Large image

![](https://guides.github.com/activities/hello-world/branching.png)


### Definition lists can be used with HTML syntax.

<dl>
<dt>Name</dt>
<dd>Godzilla</dd>
<dt>Born</dt>
<dd>1952</dd>
<dt>Birthplace</dt>
<dd>Japan</dd>
<dt>Color</dt>
<dd>Green</dd>
</dl>

```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```

```
The final element.
```
-->

