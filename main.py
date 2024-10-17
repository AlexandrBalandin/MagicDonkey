import vk_api
import random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

token = "vk1.a.uqqH8l7UAu6ld8oCpBsVtsf6M4jpU3VxLEe_TQvru5vaoVl1tNXeOe5GVO4q03zsva6gxcLTOIGpxn6Lfa-hCeJJZJq5o6ZBQGGHrtwx_WTtTPj3O1HFeUA2xxOxnsiWn8WPnweS1BoYoGab9c7v1adgsrWso1XdRaIe56B8T6MvmYbvZHVFUb2rOnbh8iGHLEO6xrADhwpVjRwdTGak_w"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
botLongPool = VkBotLongPoll(vk, 227770673, 25)


def writeUserMsg(from_id, random_id, message):
    vk.method('messages.send', {'user_id': from_id,
                                'message': message,
                                'random_id': random_id,
                                })


def writeChatMsg(peer_id, random_id, message):
    vk.method('messages.send', {'message': message,
                                'random_id': random_id,
                                'peer_id': peer_id})


def diceAnswer(mess, peer_id, random_id):
    if (mess.find('д100')) or (mess.find('к100')):
        writeChatMsg(peer_id,
                     random_id,
                     'Тебе выпадает: ' + str(random.randint(1, 100)))
    elif (mess.find('д4')) or (mess.find('к4')):
        writeChatMsg(peer_id,
                     random_id,
                     'Тебе выпадает: ' + str(random.randint(1, 4)))
    elif (mess.find('д6')) or (mess.find('к6')):
        writeChatMsg(peer_id,
                     random_id,
                     'Тебе выпадает: ' + str(random.randint(1, 6)))
    elif (mess.find('д8')) or (mess.find('к8')):
        writeChatMsg(peer_id,
                     random_id,
                     'Тебе выпадает: ' + str(random.randint(1, 8)))
    elif (mess.find('д10')) or (mess.find('к10')):
        writeChatMsg(peer_id,
                     random_id,
                     'Тебе выпадает: ' + str(random.randint(1, 10)))
    elif (mess.find('д12')) or (mess.find('к12')):
        writeChatMsg(peer_id,
                     random_id,
                     'Тебе выпадает: ' + str(random.randint(1, 12)))
    else:
        writeChatMsg(peer_id,
                     random_id,
                     'Тебе выпадает: ' + str(random.randint(1, 20)))


def listenMessage():
    writeChatMsg('2000000002', 0, 'Стартуем, епта')
    # Основной цикл
    for event in botLongPool.listen():
        print(event)
        if event.type == VkBotEventType.MESSAGE_NEW:

            # Достаем сообщения из чата
            if event.from_chat:
                mess = event.object.message['text'].lower()
                if (mess.find('каст') != -1):
                    writeChatMsg(event.object.message['peer_id'],
                                 event.object.message['random_id'],
                                 'Ты не достоин кастовать(еще не реализовано)')

                if (mess.find('кида') != -1) or (mess.find('брос') != -1):
                    diceAnswer(
                        mess, event.object.message['peer_id'], event.object.message['random_id'])

            # Личные сообщения боту(извращенцы)
            elif event.from_user:
                writeUserMsg(event.object.message['from_id'],
                             event.object.message['random_id'],
                             event.object.message['text'])

        else:
            None


listenMessage()
