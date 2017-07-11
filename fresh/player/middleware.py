class playermiddleware:
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path not in ['/player/register/',
                                '/player/player_zc/',
                                '/player/player_name/',
                                '/player/login/',
                                '/player/login_yz/',
                                '/player/login_out/',]:
            request.session['player_path'] = request.get_full_path()