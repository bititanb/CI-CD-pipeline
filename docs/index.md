---
layout: default
---

baseurl: /CI-CD-pipeline

## Что это?

Proof-of-Concept автоматизированного развертывания CI/CD и приложения в нём.<br>
Развертывание полностью автоматическое ([быстрый старт с Vagrant](https://github.com/bititanb/CI-CD-pipeline)).
TODO [Быстрый старт]

## Стек

| Vagrant/VirtualBox или Packer/KVM | Создание VM                                                    |
| Ansible                           | Развертывание инфраструктуры И приложения                      |
| Jenkins                           | Сборка/тесты/деплой с использованием Ansible[*](#ansible-note) |
| Kubernetes/Docker                 | Контейнеризация приложения                                     |
| Zabbix                            | Мониторинг                                                     |
| ELK/Filebeat                      | Логирование                                                    |
| Django/Bootstrap/Postgres/Nginx   | Приложение                                                     |

Стек подобран просто по распространенности, некоторый софт я бы заменил.

## Как сделано?

Развертывания инфраструктуры и, при новых коммитах, приложения:

![Add Remove Programs]({{'/assets/img/vagrantup.plain.svg' | absolute_url}} "Add Remove Programs")
![ERROR: Can't display image.](/assets/img/vagrantup.plain.svg)

Т. к. это демонстрация, некоторое сделано иначе/проще, чем должно быть. К примеру, само приложение и зависимые сервисы (БД, reverse proxy, почт. сервер) находятся в одном [kubernetes pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/#what-is-a-pod), т.е. дублируются для каждой его реплики, при том БД контейнеризованы (что для боевых условий не годится).  

Но иногда были и просто плохие решения, как пример — Ansible-роль вместо Groovy/shell-скриптов для сборки/тестирования/деплоя (было настолько медленно, что пришлось отключить все зависимости от других ролей, а без этого Ansible не нужен). В подобных случаях, если переделывание требовало много времени, оставлял как есть, пока работает.
{: #ansible-note}

В целом, с оглядкой на то, что это демо, сделано прилично.

## Как это выглядит

4-х минутный монтаж развертывания с нуля и проверки работоспособности (в реальном времени ~30-40 минут на моей машине):

<iframe src="https://player.vimeo.com/video/240532809" width="960" height="540" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

## Более подробный обзор

<!-- <iframe width="960" height="740" marginheight="0" marginwidth="0" src="http://localhost:8000"> -->
  <!-- Iframe can't be loaded. -->
<!-- </iframe> -->


## Быстрый старт
TODO

## Github
TODO




















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

