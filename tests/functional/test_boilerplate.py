def test_django_bootstrap_app_installed(settings):
    assert "django_bootstrap_app" in settings.INSTALLED_APPS
