# coding=utf-8

from .base import BaseHandler
from models.grade import Grade
from utils.check import require_login


class GradeHandler(BaseHandler):
    @require_login
    def post(self, uid):
        """
        @apiDescription 提交新的评分
        @api {post} /user/([0-9]+)/foods/grades/? 提交新的评分
        @apiGroup grade

        @apiParam {Number} fid 食品id
        @apiParam {Number} [score] 评分
        @apiParam {String} [comment] 评论
        @apiParam {Number} [speed] 配送时间

        @apiPermission user

        @apiSuccess {Number} gid 评分id
        """
        uid = self.get_current_user()
        fid = int(self.get_argument("fid"))
        score = float(self.get_argument("score", 4.0))
        score = score if score < 5 else 5  # 5分制
        comment = self.get_argument("comment", "好评")
        speed = int(self.get_argument("speed", 20))

        grade = Grade(fid=fid, uid=uid, score=score, comment=comment, speed=speed)
        self.orm_session.add(grade)
        self.orm_session.commit()
        self.write(dict(
            gid=grade.id
        ))

    @require_login
    def delete(self, uid):
        """
        @apiDescription 删除评分
        @api {delete} /user/([0-9]+)/foods/grades/? 删除评分
        @apiGroup grade

        @apiPermission user
        """
        gid = int(self.get_argument("gid"))
        uid = self.get_current_user()

        Grade.delete(self.orm_session, uid, gid)
        self.write({})
