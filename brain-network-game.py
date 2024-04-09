import json
import time


def load_game_data():
    """
    从 JSON 文件中读取游戏数据，得到的数据类型为 dictionary
    """
    with open('./data.json', 'r', encoding='utf8') as fp:
        data = json.load(fp)
    return data


def display_line(text, delay=0.05):
    """
    逐字显示文本，用 sleep 间隔
    """
    for word in text:
        print(word, end="")
        time.sleep(delay)
    print()

def display_scene_texts(lines, delay=0.05):
    """
    逐行显示文本，用 sleep 间隔
    """
    print()
    for line in lines:
        display_line(line)
        time.sleep(delay)


def display_prompts(prompts):
    print()
    for prompt in prompts:
        print('%s 【%s】' % (prompt['text'], prompt['answer'].upper()))
    print('退出游戏 【Q】')
    print()


def display_scene(scenes, scene_name):
    """
    显示游戏场景
    :scenes 全部游戏场景数据 dictionary
    :scene_name 当前场景名称 str
    """

    scene = scenes[scene_name]  # 找到当前场景

    display_scene_texts(scene['scene_texts'])

    if 'is_end' in scene:  # 判断是否为结局场景
        print('\n%s\n' % scene['end_text'])
        return

    prompts = scene['prompts']  # 获取当前场景的提问列表
    display_prompts(prompts)
    
    # 接收用户输入
    c = input('请输入你的选择：')
    time.sleep(0.5)
    user_choice = None

    while (user_choice is None):

        if c.upper() == 'Q':
            break

        for prompt in prompts:  # 在提问列表里查找正确答案
            if c.upper() == prompt['answer'].upper():
                user_choice = prompt
                break

        if user_choice is None:
            display_prompts(prompts)
            c = input('请输入你的选择：')

    # go to next scene
    if user_choice is not None:
        display_scene_texts(prompt['texts_after_action'])
        next_scene_name = prompt['next_scene']  # 得到下一场景的名称
        display_scene(scenes, next_scene_name)  # 去下一个场景

def main():
    print('加载数据，请稍后...', end='')
    time.sleep(1)
    data = load_game_data()  # 加载游戏数据
    print('完成')

    print('\n欢迎来到%s\n' % data['name'])

    scenes = data['scenes']       # 全部游戏场景
    start_scene_name = 'scene01'  # 第一个场景名称

    display_scene(scenes, start_scene_name)  # 开始游戏，显示第一个场景


if __name__ == '__main__':
    main()
