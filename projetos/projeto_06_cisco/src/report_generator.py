from jinja2 import Template


def generate_html(df):

    html_template = """
    <html>
    <body>

    <h1>Inventário Cisco</h1>

    {{ table }}

    </body>
    </html>
    """

    template = Template(html_template)

    html = template.render(
        table=df.to_html(index=False)
    )

    with open(
        "reports/inventory.html",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)