const language_selectors = document.querySelectorAll(".village-translate__language")

language_selectors.forEach(el => el.addEventListener("click", event => {
    document.cookie = "django_language=" + el.lang + ";Path=\"/django-village\";SameSite=Strict"
    window.location.reload()
}));
