from channels.routing import ProtocolTypeRouter
from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

application = ProtocolTypeRouter({
	'websocket': AllowedHostsOriginValidator(
		AuthMiddlewareStack(
			URLRouter(
				[
					url()
				]
			)
		)
	)
})
