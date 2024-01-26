template = """
<html>
    <ul>
    {% for t in todos %}
        <div>
        {% if t.important is True %}
            {{ t.task }}
        {% endif %}
        </div>
    {% endfor %}
    </ul>
</html>
"""