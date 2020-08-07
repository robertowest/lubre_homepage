select * from homepage_entries;

-------------------
-- homepage_entries
-------------------

-- homepage
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('Inicio','#home','homepage/_header.html',NULL,1,1,'home');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('Nosotros','#about','homepage/_about.html',NULL,2,1,'home');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('Servicio','#service','homepage/_service.html',NULL,3,1,'home');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('Equipo','#team','homepage/_team.html',NULL,4,1,'home');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('separador',NULL,'homepage/_separator_1.html',NULL,5,1,'home');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('¿Por qué elegirnos?',NULL,'homepage/_why_choose_us.html',NULL,6,0,'home');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('video',NULL,'homepage/_video.html',NULL,7,1,'home');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('Catálogo','#catalog','homepage/_catalog.html',NULL,8,1,'home');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('Proyectos',NULL,'homepage/_project.html',NULL,9,1,'home');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('Testimonio','#testimonial','homepage/_testimonial.html',NULL,10,1,'home');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('Precios',NULL,'homepage/_pricing.html',NULL,11,0,'home');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('separador2',NULL,'homepage/_separator_2.html',NULL,12,1,'home');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('Blog','#blog','homepage/_blog.html',NULL,13,1,'home');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('Contacto','#contact','homepage/_contact.html',NULL,14,1,'home');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('pie de página superior',NULL,'homepage/_footer_top.html',NULL,15,1,'home');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('pie de página inferior',NULL,'homepage/_footer_bottom.html',NULL,16,1,'home');

-- acerca de nosotros
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES (
'Acerca de nosotros ...','Bienvenido a <span>Lubre SRL</span>','Para alcanzar una posición más competitiva dentro de nuestra actividad buscamos la transformación de nuestra estructura organizacional adaptándola a las exigencias del mercado. Para ello identificamos que nuestro propósito es:<br><br>
<b>Ser una empresa sustentable a partir de entregar una propuesta de valor a nuestros clientes, desarrollar las capacidades de nuestros colaboradores y obtener el reconocimiento de nuestra comunidad.</b><br><br>
Para llevar adelante, hemos definido las bases que identifican y orientan nuestro actuar. A partir de la incorporación de nuevas unidades de negocio hemos planteado nuestra MISION y VISION para toda la organización.','',1,1,'about');

-- por qué nosotros?
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES (
'Misión de la Organización',NULL,'Somos una empresa que a través de la distribución de productos YPF, busca satisfacer a la clientela brindando un servicio de excelencia a partir del desarrollo de nuestros recursos humanos, de una estructura adecuada y alineada a la estrategia de nuestro principal proveedor, buscamos a partir de resultados, maximizar nuestro desempeño organizacional.',NULL,1,1,'whyus');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES (
'Visón de la Organización',NULL,'Ser una empresa solida, que a partir de conformar una alianza estratégica con nuestro principal proveedor, de su accionar con elevados estándares éticos y profesionales, y de su desempeño eficiente, y de la entrega de un servicio diferenciado sea reconocida y elegida por el mercado tucumano.',NULL,2,1,'whyus');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES (
'Nuestros Valores',NULL,'<b>Compromiso</b>: Con los objetivos y valores de la organización.<br>
<b>Responsabilidad</b>: Para utilizar todas las capacidades para cumplir con la tarea asignada.<br>
<b>Profesionalismo</b>: Que implica desempeñarse con idoneidad en sus tareas para lo cual se fomenta la capacitación permanente.<br>
<b>Solidaridad</b>: Para desarrollar un ambiente laboral que promueva el bienestar de todos los integrantes y propicie la relación con la comunidad.<br>
<b>Sentido de pertenencia</b>: Entendido como identificación con la cultura de la organización.<br>
<b>Transparencia</b>: Para difundir información adecuada, fiel y veraz de la gestión. Comunicación clara tanto interna como externa.<br>
<b>Trabajo en equipo</b>: Como una manera de afrontar el desafío laboral.',NULL,3,1,'whyus');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES (
'RRHH',NULL,'El perfil de nuestros colaboradores se define por su iniciativa, capacidad de trabajo en equipo, resolución de problemas, toma de decisiones, predisposición al aprendizaje y confiabilidad.',NULL,4,1,'whyus');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES (
'Recursos Materiales',NULL,'Para desarrollar una gestión eficiente, nuestra organización considera de fundamental importancia contar con los recursos materiales y la tecnología necesaria para garantizar el cumplimiento de sus objetivos. Para ello disponemos de: Instalaciones: un local de ventas y oficinas administrativas ubicadas en el microcentro de San Miguel de Tucumán y un predio de casi 2 Has donde se ubica además de 600 metros cuadrados de oficinas administrativas, la planta de gas oil y el depósito de 650 metros cuadrados destinado al almacenamiento de lubricantes, fertilizantes y agroquímicos; este predio esta ubicado a 4 km de las cuidad sobre Ruta Nacional N° 9 - autopista.',NULL,5,1,'whyus');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES (
'Equipos',NULL,'Para la distribución de nuestros productos contamos con camionetas y camiones especialmente adaptados para estas tareas.',NULL,6,1,'whyus');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES (
'Tecnología',NULL,'Contamos con tecnología de punta en nuestro sistema informático para poder mantener la fluidez de nuestra comunicaciones y brindar un servicio diferenciado a nuestros clientes .',NULL,7,1,'whyus');

-- servicios
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES (
'YPF Agro',NULL,'Cada campo necesita algo diferente. Por eso decidimos tenerlo todo.','agro',1,1,'service');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES (
'Oil & Gas',NULL,'Producto y servicio hasta el punto de producción industrial.','lubricante',2,1,'service');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES (
'Estación de Servicio',NULL,'Visitá nuestras estaciones de servicio y conocé todos los beneficios que tenemos para vos.','full',3,1,'service');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES (
'Logística',NULL,'La elección mas conveniente para el transporte.​ ','logistica',4,1,'service');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES (
'Construcción',NULL,'Lideres en comercialización de asfaltos e insumos energéticos para la construcción.','construccion',5,1,'service');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES (
'Gas',NULL,'La solución para los clientes de GLP envasado.','combustible',6,1,'service');



-- catálogo
INSERT INTO homepage_entries ("section",label,text_short,ordered,active) VALUES ('catalogTag','Todos','*',1,1);
INSERT INTO homepage_entries ("section",label,text_short,ordered,active) VALUES ('catalogTag','Agro','.agro',2,1);
INSERT INTO homepage_entries ("section",label,text_short,ordered,active) VALUES ('catalogTag','Combustible','.combustible',3,1);
INSERT INTO homepage_entries ("section",label,text_short,ordered,active) VALUES ('catalogTag','Lubricante','.lubricante',4,1);
INSERT INTO homepage_entries ("section",label,text_short,ordered,active) VALUES ('catalogTag','Fertilizante','.fertilizante',5,1);

INSERT INTO homepage_entries ("section",label,text_short,text_large,image,ordered,active) VALUES ('catalog', 'Infinia',       'Combustibles','combustible infinia','catalog/infinia.jpg',1,1);
INSERT INTO homepage_entries ("section",label,text_short,text_large,image,ordered,active) VALUES ('catalog', 'Infinia Diesel','Combustibles','combustible infinia diesel','catalog/indinia-diesel.jpg',2,1);
INSERT INTO homepage_entries ("section",label,text_short,text_large,image,ordered,active) VALUES ('catalog', 'Nafta Super',   'Combustibles','combustible','catalog/nafta-super.jpg',3,1);

INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('ELAION','Lubricantes','lubricante','catalog/3.jpg',3,1,'catalog');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('Best Air','Aromatizador','lubricante','catalog/4.jpg',4,1,'catalog');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('Bolsas','Bolsas para silos','agro','catalog/5.jpg',5,1,'catalog');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('Cipermetrina','Agroquímicos','agro','catalog/6.jpg',6,1,'catalog');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('Plus Soliar','Agroquímicos','agro',Null,7,1,'catalog');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('Cloruro de Potasio','Fertilizantes','agro',Null,8,1,'catalog');
INSERT INTO homepage_entries (label,text_short,text_large,image,ordered,active,"section") VALUES ('Nitrato de Plata','Fertilizantes','agro',Null,9,1,'catalog');


-- testimonios de clientes
INSERT INTO homepage_entries ("section",label,text_short,text_large,image,ordered,active)
VALUES ('message','Jon Doe','CEO of Google','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s.','message/3.jpg',1,1);
INSERT INTO homepage_entries ("section",label,text_short,text_large,image,ordered,active)
VALUES ('message','Michael Schumacher','CEO of Microsoft','Pellentesque in dolor sed turpis posuere bibendum a sed lorem. Quisque sagittis mauris vel viverra auctor.','message/2.jpg',2,1);
INSERT INTO homepage_entries ("section",label,text_short,text_large,image,ordered,active)
VALUES ('message','Vanesa Williams','CEO of Oracle','Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Ut convallis dignissim libero, eu tempus tortor ultricies vitae. Curabitur aliquam neque sed lacus consectetur, sit amet interdum lacus vulputate. Quisque et nulla vel est gravida blandit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus quis eleifend mauris. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nullam rhoncus ligula non dolor dignissim bibendum. Praesent consequat est ligula.','message/1.jpg',3,1);




--------------------
-- homepage_category
--------------------
INSERT INTO homepage_category (name) VALUES ('Sin Categoría');
INSERT INTO homepage_category (name) VALUES ('Combustibles');
INSERT INTO homepage_category (name) VALUES ('Lubricantes');
INSERT INTO homepage_category (name) VALUES ('Agroquímicos');



---------------
-- homepage_tag
---------------
INSERT INTO homepage_tag (name) VALUES ('Noticias');
INSERT INTO homepage_tag (name) VALUES ('Ofertas');



----------------
-- homepage_post
----------------
INSERT INTO homepage_post (title,slug,content,image,created_on,updated_on,author_id,category_id,publish_on) VALUES (
'despedida de soltera','despedida-de-soltera','Alguien grabó el momento en el que la mujer, apodada Lady Coralina, se besa apasionadamente con un muchacho en su fiesta en Playa del Carmen.<br><br>
En general son las mujeres las que le temen a la despedida de soltero de sus futuros maridos: bromas demasiado pesadas, mujeres de piernas ligeras y lugares non sanctos son la pesadilla de las novias. Pero no hay que discriminar: las novias también pueden ser infieles y así lo demuestra la última estrella viral, Lady Coralina. <br><br>
Ella se llama Emma Alicia Paz Ayala y celebró su despedida de soltera en Playa del Carmen. Pero algunos tragos, le emoción del momento (?) o el ritmo de la música (!) la llevaron a besarse con otro chico. Claro, no era su novio.','blog/blog1.jpg','2019-11-07','2019-11-07',1,NULL,'2019-11-07');
INSERT INTO homepage_post (title,slug,content,image,created_on,updated_on,author_id,category_id,publish_on) VALUES (
'Importante','importante','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue nulla. Maecenas sit amet ligula est. Fusce fringilla sollicitudin enim in varius. Praesent nisi neque, condimentum sit amet lacus inLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue nulla. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue nulla. Maecenas sit amet ligula est. Fusce fringilla sollicitudin enim in varius. Praesent nisi neque, condimentum sit amet lacus inLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue nulla. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue nulla. Maecenas sit amet ligula est. Fusce fringilla sollicitudin enim in varius. Praesent nisi neque, condimentum sit amet lacus inLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue nulla. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue nulla. Maecenas sit amet ligula est. Fusce fringilla sollicitudin enim in varius. Praesent nisi neque, condimentum sit amet lacus inLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue nulla.','blog/blog2.jpg','2019-11-07','2019-11-07',1,NULL,'2019-10-01');
INSERT INTO homepage_post (title,slug,content,image,created_on,updated_on,author_id,category_id,publish_on) VALUES (
'Segundo','segundo','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue nulla. Maecenas sit amet ligula est. Fusce fringilla sollicitudin enim in varius. Praesent nisi neque, condimentum sit amet lacus inLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue nulla. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue nulla. Maecenas sit amet ligula est. Fusce fringilla sollicitudin enim in varius. Praesent nisi neque, condimentum sit amet lacus inLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue nulla. Lorem ipsum dolor sit amet.
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue nulla. Maecenas sit amet ligula est. Fusce fringilla sollicitudin enim in varius. Praesent nisi neque, condimentum sit amet lacus inLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue nulla. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue nulla. Maecenas sit amet ligula est. Fusce fringilla sollicitudin enim in varius. Praesent nisi neque, condimentum sit amet lacus inLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue nulla. Lorem ipsum dolor sit amet.','blog/blog3.jpg','2019-11-07','2019-11-07',1,NULL,'2019-10-20');
INSERT INTO homepage_post (title,slug,content,image,created_on,updated_on,author_id,category_id,publish_on) VALUES (
'Borra de Café','borra-de-cafe','bla bla bla','blog/borra-de-cafe.jpg','2019-11-07','2019-11-07',1,NULL,'2019-11-07');
INSERT INTO homepage_post (title,slug,content,image,created_on,updated_on,author_id,category_id,publish_on) VALUES (
'Escanea y pagá','escanea-y-paga','ESCANEÁ Y PAGÁ CON TU CELULAR.<br>
Nuevo servicio en YPF Ruta 5 (9 de Julio) !!!<br><br>
Cargá combustible ⛽️ y pagá con código QR, también podés usarlo para tus compras en FULL<br><br>
Descargá la app de YPF 📲 y accedé a importantes beneficios.<br><br>
Próximamente estará habilitado en todas nuestras estaciones de servicio.','blog/escaneas.jpg','2019-11-07','2019-11-07',1,NULL,'2019-11-07');



---------------------
-- homepage_post_tags
---------------------
INSERT INTO homepage_post_tags (post_id,tag_id) VALUES (4,1);
INSERT INTO homepage_post_tags (post_id,tag_id) VALUES (5,1);
