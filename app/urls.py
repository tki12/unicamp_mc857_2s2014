# !/usr/bin/python
# coding=utf-8

from django.conf.urls import patterns, url

from app import views, controls, apis

urlpatterns = patterns('',
	# View URLs
	url(r'^$', views.home, name='view.home'),
	url(r'^usuario/entrar/?$', views.userLogin, name='view.user.login'),
	url(r'^usuario/perfil/(?P<username>[a-z-A-Z0-9\ \- \+\_]+)/?$', views.userProfile, name='view.user.profile'),
	url(r'^usuario/perfil/atualizar/?$', views.userProfileUpdate, name='view.user.update'),
	url(r'^usuario/registrar/?$', views.userRegister, name='view.user.register'),
	url(r'^usuario/avaliar/?$', views.userReview, name='view.user.review'),
	url(r'^rota/adicionar/?$', views.routeAdd, name='view.route.add'),
	url(r'^rota/detalhar/(?P<rotaID>[0-9]+)?$', views.routeDetail, name='view.route.detail'),
	url(r'^rota/gerenciar/?$', views.routeManage, name='view.route.manage'),
	url(r'^rota/buscar/?$', views.routeSearch, name='view.route.search'),
	url(r'^rota/atualizar/(?P<rotaID>[0-9]+)/?$', views.routeUpdate, name='view.route.update'),
	# Control URLs
	url(r'^controle/usuario/bloquear/?$', controls.userBlock, name='view.user.block'),
	url(r'^controle/usuario/contatar/?$', controls.userContact, name='control.user.contact'),
	url(r'^controle/usuario/login/?$', controls.userLogin, name='control.user.login'),
	url(r'^controle/usuario/atualizar/?$', controls.userProfileUpdate, name='control.user.update'),
	url(r'^controle/usuario/registrar/?$', controls.userRegister, name='control.user.register'),
	url(r'^controle/usuario/avaliar/?$', controls.userReview, name='control.user.review'),
	url(r'^controle/rota/adicionar/?$', controls.routeAdd, name='control.route.add'),
	url(r'^controle/rota/remover/?$', controls.routeRemove, name='control.route.remove'),
	url(r'^controle/rota/buscar/?$', controls.routeSearch, name='control.route.search'),
	url(r'^controle/rota/atualizar/?$', controls.routeUpdate, name='control.route.update'),
	# API URLs
# 	url(r'^/?$', apis., name='api.'),
)
