# -*- coding: utf-8 -*-
import re

s = "\n\r\t@#$%^&*这样一本书大卖，有点意外，据说已经印了四五十万，排行榜仅次于《希拉里自传》。大概是大众抛弃了一位表演过火的“文化大师”后，需要再找一位有格调的“文化饰品”来装点吧？书的装帧果然有品格，书皮是淡棕色的皱纹纸，书摊老板告诉我这纸是进口的。有一个加印版是绿色封皮，差很多。开始出于对热买书的反感，没有下手。虽然很喜欢作者，但近两年，买了一些早先钟爱的作家的新作，大失所望，故此这次谨慎很多。单位主编买了一本，边审节目边看，泪水涟涟（这位领导为四十出头的女性）。干脆借来一观。半天一口气读完大半，晚上睡前读完了。睡时心里像纠了一个结，很像以前特投入地读完一本武侠书，怅然若失，随着最后一页书合上，一个世界也合上了大门。杨绛的以前的书基本都读过，包括钱钟书题写书名的三卷集，写知识分子思想改造、反右干校，写她父亲的文章印象特别深刻。但从没有像这本书，整本笔墨都是在写她最亲的两个人，丈夫和女儿。以往一直觉得杨绛的笔锋有点像奥斯丁，用很干净疏朗的笔法写身边琐事，即使是大事变，捕捉的也是实实在在的细处。以前的印象是冷静，情绪流露虽只是轻轻点一下，但仍透着一股贵族气在里头。有一位知青作家就特受不了，譬如《干校六记》中的一处，写她路见一落魄小将，如狼崽子一般，心下不由生出点快意。钱钟书的夫人自然是有傲气的。但《我们仨》太不一样了，记述她女儿罹患恶疾病故的那一章（第二部分），那种痛楚简直是倾泻纸面，虽然作者故意采用梦境式的虚幻技巧（这一手法她在《将饮茶》中已经牛刀小试，这里已经成演变为独立的一章了），想造成间离（估计老太太自己也受不了直接面对这段时间），但依然能见到处处泪渍，大概很少有读者能经受得起。我也步了女主编的后尘。有位老前辈评点说，杨绛的这本新书是她最差的一本，或许指的就是这点吧。在时人看来，让人掉眼泪的书似乎品格有问题。第三部分又回到了杨绛的一贯笔法，记述和钱钟书、钱媛共度的岁月，流畅极了，很好读，一个大学者原来是那么童稚的一个人，在书中，一家三口的心性似乎永远停留在那段黄金岁月：即封面那张四十年代的合影，圆圆。七十岁的老人、五十多岁的女儿，依旧开着五十年前的玩笑，太动人了。我就像在观看神仙的游戏。最后老太太淡淡记道：现在只剩下我一个人，怀念着我们仨。我是打乱次序读，先读第一部分（序），随后是第三部分，第二部分，反而印象比较好。或许顺着读，先撕心裂肺痛了一下，效果并不佳。推荐倒着看。\n\s\r\t"
t= re.findall('[\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b\u4e00-\u9fa5]',s)
#                  。     ；     ，    ：    “     ”     （     ）    、    ？   《      》


print(''.join(t))
