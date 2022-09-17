import numpy as np
from OpenGL.GL import *
class BufferObject:
    def __init__(self, buffer, type, drawtype) -> None:
        self.buffer = buffer
        self.type = type
        self.drawtype = drawtype
    def bind(self):
        glBindBuffer(self.type, self.buffer)
    def unbind(self):
        glBindBuffer(self.type, 0)
    def data(self, data):
        glBufferData(self.type, data, self.drawtype)
    def __del__(self):
        self.unbind()
        glDeleteBuffers(1, [self.buffer])

class VBO(BufferObject):
    def __init__(self, data=None) -> None:
        self.buffer = glGenBuffers(1)
        super().__init__(self.buffer, GL_ARRAY_BUFFER, GL_STATIC_DRAW)
        self.auto(data)
    def auto(self, data):
        if data is not None:
            self.bind()
            self.data(np.array(data, dtype=np.float32))
            self.unbind()

class IBO(BufferObject):
    def __init__(self, data=None) -> None:
        self.buffer = glGenBuffers(1)
        super().__init__(self.buffer, GL_ELEMENT_ARRAY_BUFFER, GL_STATIC_DRAW)
        self.auto(data)
    def auto(self, data):
        if data is not None:
            self.bind()
            self.data(np.array(data, dtype=np.int32))
            self.unbind()

class VAO:
    def __init__(self) -> None:
        self.buffer = glGenVertexArrays(1)
    def loadBufferToAttribLocation(self, attrNum, bufferObject, ddim=3, dtype=GL_FLOAT, normalized=GL_FALSE, stride=0, pointer=None):
        self.bind()
        bufferObject.bind()
        glEnableVertexAttribArray(attrNum)
        glVertexAttribPointer(attrNum, ddim, dtype, normalized, stride, pointer)
        self.unbind()
        del bufferObject
    def loadIndices(self, bufferObject):
        self.bind()
        bufferObject.bind()
        self.unbind()
        del bufferObject
    def bind(self):
        glBindVertexArray(self.buffer)
    def unbind(self):
        glBindVertexArray(0)
    def __del__(self):
        self.unbind()
        glDeleteVertexArrays(1, [self.buffer])