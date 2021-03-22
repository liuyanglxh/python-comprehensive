from forjob.my_cache.localcache import mem_cache

class Ebk5BookService(object):
    @mem_cache(7200,'',1000000000)
    def book_name_rel_id(self):
        '''
        书名与书籍ID映射关系
        '''
        bk_list = Ebk5Book.mgr(ismaster=True).raw("select bookName,ID from ebk5_book")
        return {i.get("bookName").lstrip('《').rstrip('》'):i.get("ID") for i in bk_list if i}

class Ebk5BookService(object):
    def get_id_by_name(self,name):
        '''
        根据书籍名称获取书籍ID
        '''
        book_id = 0
        bk_rel_dict = self.book_name_rel_id()
        if bk_rel_dict.has_key(str(name)):
            book_id = bk_rel_dict.get(str(name))
        return book_id
