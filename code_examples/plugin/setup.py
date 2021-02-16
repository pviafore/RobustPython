from setuptools import setup

setup(
    name='ultimate-kitchen-assistant',
    version='1.0',

    description='Ultimate Kitchen Assistant',

    author='Pat Viafore',
    author_email='pat@kudzera.com',
    packages=["ultimate_kitchen_assistant"],
    include_package_data=True,
   
    entry_points={
        'ultimate_kitchen_assistant.recipe_maker': [
            'pasta_maker = ultimate_kitchen_assistant.pasta_maker:PastaModule',
            'tex_mex = ultimate_kitchen_assistant.tex_mex:TexMexModule'
        ],
    },
)
