from flask import Flask

# .bg_frame_01{
# /*    background: #0000AA; */
# background: #663333;
# border-radius: 30%;
# box-shadow: 14.41px 14.41px 19px #4D2727, -14.41px -14.41px 19px #7F3F3F;
# }

# .bg_frame_02 {
# background: linear-gradient(145deg, #572B2B, #753B3B);
# border-radius: 15%;
# box-shadow: 14.41px 14.41px 19px #4D2727, -14.41px -14.41px 19px #7F3F3F;
# }


# html_str = '''
# <body style="background: linear-gradient(145deg, #572B2B, #753B3B);border-radius: 4%;box-shadow: 14.41px 14.41px 19px #000080, -14.41px -14.41px 19px #0000D4;padding: 2%;margin:2%">
# <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed gravida lorem, id pharetra tellus. Aenean tincidunt laoreet orci. Pellentesque condimentum urna ligula. In eget risus in quam commodo blandit. Praesent faucibus placerat interdum. Vestibulum ultrices sit amet mauris eget lobortis. Ut volutpat maximus consectetur. Quisque eget tempor nibh.</p>
# </body>
# '''



app = Flask(__name__)

html_str = '''
<html>
<head>
<style>
body {
    color: #00009C;
    background: #663333;border-radius: 20px;
#   box-shadow: 14.41px 14.41px 44px #422121, -14.41px -14.41px 44px #8A4545;
    box-shadow: 14.41px 14.41px 44px #582C2C, -14.41px -14.41px 44px #743A3A;
    padding: 10px;margin:10px

}
div {
    background: #663333;
    box-shadow: 14.41px 14.41px 44px #331A1A, -14.41px -14.41px 44px #994D4D;    
    border-radius: 20px;
    padding: 3px 1px 25px 5px;
    margin: 15px 1px 25px 20px;
}
p {
    background: #00001A;
    color: #8888FF;
    padding: 2em;
    margin: 1em;
    border-radius: 20px;
}
h1 {
    text-align: left;
    background: #440000;
    margin: 10px 60% 0px 10px;
    padding: 10px 10px 10px 20px;
    color: #B37373;
    box-shadow: 14.41px 14.41px 44px #582C2C, -14.41px -14.41px 44px #743A3A;
    border-radius: 20px;
}
</style>
</head>
<body>
    <div>
        <h1>Heading</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed gravida lorem, id pharetra tellus. Aenean tincidunt laoreet orci. Pellentesque condimentum urna ligula. In eget risus in quam commodo blandit. Praesent faucibus placerat interdum. Vestibulum ultrices sit amet mauris eget lobortis. Ut volutpat maximus consectetur. Quisque eget tempor nibh.</p>
        <div>
            <h1>Heading</h1>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed gravida lorem, id pharetra tellus. Aenean tincidunt laoreet orci. Pellentesque condimentum urna ligula. In eget risus in quam commodo blandit. Praesent faucibus placerat interdum. Vestibulum ultrices sit amet mauris eget lobortis. Ut volutpat maximus consectetur. Quisque eget tempor nibh.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed gravida lorem, id pharetra tellus. Aenean tincidunt laoreet orci. Pellentesque condimentum urna ligula. In eget risus in quam commodo blandit. Praesent faucibus placerat interdum. Vestibulum ultrices sit amet mauris eget lobortis. Ut volutpat maximus consectetur. Quisque eget tempor nibh.</p>
                <div>
                    <h1>Heading</h1>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed gravida lorem, id pharetra tellus. Aenean tincidunt laoreet orci. Pellentesque condimentum urna ligula. In eget risus in quam commodo blandit. Praesent faucibus placerat interdum. Vestibulum ultrices sit amet mauris eget lobortis. Ut volutpat maximus consectetur. Quisque eget tempor nibh.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed gravida lorem, id pharetra tellus. Aenean tincidunt laoreet orci. Pellentesque condimentum urna ligula. In eget risus in quam commodo blandit. Praesent faucibus placerat interdum. Vestibulum ultrices sit amet mauris eget lobortis. Ut volutpat maximus consectetur. Quisque eget tempor nibh.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed gravida lorem, id pharetra tellus. Aenean tincidunt laoreet orci. Pellentesque condimentum urna ligula. In eget risus in quam commodo blandit. Praesent faucibus placerat interdum. Vestibulum ultrices sit amet mauris eget lobortis. Ut volutpat maximus consectetur. Quisque eget tempor nibh.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed gravida lorem, id pharetra tellus. Aenean tincidunt laoreet orci. Pellentesque condimentum urna ligula. In eget risus in quam commodo blandit. Praesent faucibus placerat interdum. Vestibulum ultrices sit amet mauris eget lobortis. Ut volutpat maximus consectetur. Quisque eget tempor nibh.</p>
                </div>
        </div>
    </div>
    <div>
        <h1>Heading</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed gravida lorem, id pharetra tellus. Aenean tincidunt laoreet orci. Pellentesque condimentum urna ligula. In eget risus in quam commodo blandit. Praesent faucibus placerat interdum. Vestibulum ultrices sit amet mauris eget lobortis. Ut volutpat maximus consectetur. Quisque eget tempor nibh.</p>
    </div>
    <div>
        <h1>Heading</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed gravida lorem, id pharetra tellus. Aenean tincidunt laoreet orci. Pellentesque condimentum urna ligula. In eget risus in quam commodo blandit. Praesent faucibus placerat interdum. Vestibulum ultrices sit amet mauris eget lobortis. Ut volutpat maximus consectetur. Quisque eget tempor nibh.</p>
        <div>
            <h1>Heading</h1>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed gravida lorem, id pharetra tellus. Aenean tincidunt laoreet orci. Pellentesque condimentum urna ligula. In eget risus in quam commodo blandit. Praesent faucibus placerat interdum. Vestibulum ultrices sit amet mauris eget lobortis. Ut volutpat maximus consectetur. Quisque eget tempor nibh.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed gravida lorem, id pharetra tellus. Aenean tincidunt laoreet orci. Pellentesque condimentum urna ligula. In eget risus in quam commodo blandit. Praesent faucibus placerat interdum. Vestibulum ultrices sit amet mauris eget lobortis. Ut volutpat maximus consectetur. Quisque eget tempor nibh.</p>
        </div>
    </div>
</body>
'''

# box-shadow: 14.41px 14.41px 19px #000027, -14.41px -14.41px 19px #00003F;
# box-shadow: 14.41px 14.41px 19px #4D2727, -14.41px -14.41px 19px #7F3F3F;
# background: linear-gradient(145deg, #572B2B, #753B3B);
# background: #663333;
# box-shadow: 14.41px 14.41px 44px #582C2C, -14.41px -14.41px 44px #743A3A;
# box-shadow: 14.41px 14.41px 44px #000055, -14.41px -14.41px 44px #0000FF;
@app.route("/")
def hello_world():
    return html_str



