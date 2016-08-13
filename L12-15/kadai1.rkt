(define TREE '(1 (2 (3 4)) 6 (7 8 9)))
(define MYTREE '((3 5) 3 7 (4 5 7) 8)) 

(define tree-member?
  (lambda (tree value)
    (cond ((null? tree) #f)
          ((pair? tree) (or (tree-member? (car tree) value) (tree-member? (cdr tree) value)))
          (else (equal? tree value))
          )))

(tree-member? TREE 4)
(tree-member? TREE 12)
(tree-member? MYTREE 8)
(tree-member? MYTREE 9)


;その1実行結果
;#t
;#f
;#t
;#f


(define map-tree
  (lambda (function tree)
    (cond ((null? tree) '())
          ((pair? tree) (cons (map-tree function (car tree)) (map-tree function (cdr tree)) ))
          (else (function tree))
          )))

(map-tree even? TREE)
(map-tree even? MYTREE)


;その2実行結果
;(#f (#t (#f #t)) #t (#f #t #f))
;((#f #f) #f #f (#t #f #f) #t)


(define map-tree2
  (lambda (function tree)
    (cond ((null? tree) '())
          ((pair? tree) (map (lambda (tree) (map-tree2 function tree)) tree))
          (else (function tree))
          )))

(map-tree2 odd? TREE)
(map-tree2 odd? MYTREE)


;その3実行結果
;(#t (#f (#t #f)) #f (#t #f #t))
;((#t #t) #t #t (#f #t #t) #f)

    